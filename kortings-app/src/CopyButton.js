
import React, {useEffect} from "react";

function CopyButton(props) {
  
  const offers = props.selectedOffers;

  useEffect(() => {
    var textareaElement = document.querySelector('.list-share textarea')

    var boodschappenlijst = []

    offers.map(function(name, index){
      boodschappenlijst.push("* " + name['shop'] +": " +name['product'] + " - " + name['deal'] + "")
    })

    console.log(boodschappenlijst)

    textareaElement.value = boodschappenlijst.join('\r\n')
  }, [])

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
    <div className="button-cell">
      <div onClick={copyList} className="button bookmark-copy">
        <i class="ri-file-copy-2-line"></i>
        <div className="bookmark-copy-tag">kopieer lijst</div>
      </div>
    </div>
  )

}

export default CopyButton;
  