from flask import Flask, render_template, request, redirect, url_for, flash
from database import Database

app = Flask(__name__)
app.secret_key = 'mysecretkey'

def get_db():
    """
    Obtiene una instancia de la base de datos.

    Returns:
        Database: Instancia de la clase Database.
    """
    if not hasattr(Flask, 'db'):
        Flask.db = Database()
    return Flask.db

@app.route('/')
def index():
    """
    Muestra la lista de contactos.

    Returns:
        render_template: Plantilla HTML para mostrar la lista de contactos.
    """
    conn = get_db().connect()
    if conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM contacts')
        data = cur.fetchall()
        conn.close()
        return render_template('index.html', contacts=data)
    else:
        return "Error connecting to database."

@app.route('/add_contact', methods=['POST'])
def add_contact():
    """
    Agrega un nuevo contacto a la base de datos.

    Returns:
        redirect: Redirige al usuario a la página principal después de agregar el contacto.
    """
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        conn = get_db().connect()
        if conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (?, ?, ?)', (fullname, phone, email))
            conn.commit()
            conn.close()
            flash('Contacto Agregado con Éxito')
            return redirect(url_for('index'))
        else:
            return "Error connecting to database."

@app.route('/edit/<int:id>')
def edit_contact(id):
    """
    Muestra el formulario para editar un contacto.

    Args:
        id (int): ID del contacto a editar.

    Returns:
        render_template: Plantilla HTML para el formulario de edición del contacto.
    """
    conn = get_db().connect()
    if conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM contacts WHERE id = ?', (id,))
        data = cur.fetchone()
        conn.close()
        if data:
            return render_template('edit-contact.html', contact=data)
        else:
            flash('Contacto no encontrado')
            return redirect(url_for('index'))
    else:
        return "Error connecting to database."

@app.route('/update/<int:id>', methods=['POST'])
def update_contact(id):
    """
    Actualiza la información de un contacto en la base de datos.

    Args:
        id (int): ID del contacto a actualizar.

    Returns:
        redirect: Redirige al usuario a la página principal después de actualizar el contacto.
    """
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        conn = get_db().connect()
        if conn:
            cur = conn.cursor()
            cur.execute("""
                UPDATE contacts
                SET fullname = ?,
                    email = ?,
                    phone = ?
                WHERE id = ?
                """, (fullname, email, phone, id))
            conn.commit()
            conn.close()
            flash('Contacto Actualizado con Éxito')
            return redirect(url_for('index'))
        else:
            return "Error connecting to database."

@app.route('/delete/<int:id>')
def delete_contact(id):
    """
    Elimina un contacto de la base de datos.

    Args:
        id (int): ID del contacto a eliminar.

    Returns:
        redirect: Redirige al usuario a la página principal después de eliminar el contacto.
    """
    conn = get_db().connect()
    if conn:
        cur = conn.cursor()
        cur.execute('DELETE FROM contacts WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        flash('Contacto Eliminado con Éxito')
        return redirect(url_for('index'))
    else:
        return "Error connecting to database."

if __name__ == '__main__':
    app.run(port=3000, debug=True)
