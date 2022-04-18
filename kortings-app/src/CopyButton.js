function CopyButton(props) {
  
  const copyList = (e) => {
      var copyButtonElement = document.querySelector('.bookmark-copy')
      var copyDialogElement = document.querySelector('.copy-dialog')
      var wrapElement = document.querySelector('.dialog-wrap')

      var clickOutside = function(e) {
        if ( !copyDialogElement.contains(e.target) && !copyButtonElement.contains(e.target)) {
          wrapElement.removeAttribute("id") 
          if(!wrapElement.hasAttribute("id")) { // stop listening to clicks outside the dialog
            return document.removeEventListener('click', clickOutside)
          }
        }
      }  

      if(! wrapElement.hasAttribute("id")) {
        wrapElement.id = "copy-dialog-on"
        if(wrapElement.id === "copy-dialog-on") { // listen to clicks outside the dialog
          document.addEventListener('click', clickOutside) 
        }   
      }
  }

  return (
    <div>        
      <span onClick={copyList} className="button bookmark-copy">
        <i class="ri-file-copy-2-line"></i>
        <div className="bookmark-copy-tag">kopieer lijst</div>
      </span>
    </div>
  )

}

export default CopyButton;
  