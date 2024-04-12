const btnDelete= document.querySelectorAll('.btn-delete');

if(btnDelete) {
  const btnArray = Array.from(btnDelete);

  btnArray.forEach((btn) => {
    btn.addEventListener('click', (e) => {

      if(!confirm('¿Seguro de eliminar el dato?')){
        e.preventDefault();
      }

    });
  })
}