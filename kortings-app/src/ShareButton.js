import React, {useState, useEffect } from "react";

function ShareButton(props) {

    var buttonText = props.buttonText
    var infoText = props.infoText
    var shareText = "Altijd de actuele aanbiedingen van supermarkten."
    if(props.customUrl === undefined) {
      var shareUrl = window.location.href
    } else {
      var shareUrl = props.customUrl
    }
    var shareTitle = document.title
    
    const shareApi = (e) => {
        if (navigator.share) {
          navigator.share({
            title: shareTitle,
            url: shareUrl
          }).then(() => {
            console.log('Link gedeeld!');
          })
          .catch(console.error);
        } else {
          var shareButtonElement = document.querySelector('.share-button')
          var shareDialogElement = document.querySelector('.share-dialog')
          var wrapElement = document.querySelector('.dialog-wrap')
    
          var clickOutside = function(e) {
            if ( !shareDialogElement.contains(e.target) && !shareButtonElement.contains(e.target)) {
              wrapElement.removeAttribute("id") 
    
              if(!wrapElement.hasAttribute("id")) { // stop listening to clicks outside the dialog
                return document.removeEventListener('click', clickOutside)
              }
            }
          }  
    
          if(! wrapElement.hasAttribute("id")) {
            wrapElement.id = "share-dialog-on"
            if(wrapElement.id === "share-dialog-on") { // listen to clicks outside the dialog
              document.addEventListener('click', clickOutside) 
            }   
          }
        }
    }

    return (
        <div className="button-cell">
            <div onClick={shareApi} className="button share-button">
                <i className="ri-share-box-fill"></i>
                <div className="button-tag">{buttonText}</div>
            </div>
        </div>
    )
}
export default ShareButton;
