
function importData() {
  let input = document.createElement('input');
  input.type = 'file';
  input.onchange = _ => {
    // you can use this method to get file and perform respective operations
            let files =   Array.from(input.files);
            let output = document.getElementById('imported');
            output.innerHTML = files.map(f => f.name).join(', ');

            console.log(files);
            

            }
       
  input.click();
  
 };