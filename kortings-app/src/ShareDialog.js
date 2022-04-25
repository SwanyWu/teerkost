function ShareDialog(props) {
  
  var buttonText = props.buttonText
  var infoText = props.infoText
  var shareText = "Altijd de actuele aanbiedingen van supermarkten."
  var shareUrl = window.location.href
  var shareTitle = document.title

  const copyMe = () => {
    var linkElement = document.querySelector(".url-share input");
    navigator.clipboard.writeText(linkElement.value); 
    console.log(shareUrl + " gekopieerd")
    var confirmElement = document.querySelector(".url-share .copy-confirm")
    confirmElement.classList.add("hide"); // reset animation
    void confirmElement.offsetWidth; // trigger reflow
    setTimeout(function(){
    confirmElement.classList.remove("hide"); // start animation
    }, 3000);
  }

  const copyMeTextarea = () => {
    var linkElement = document.querySelector(".list-share textarea");
    navigator.clipboard.writeText(linkElement.value);
    console.log("Bewaarlijst gekopieerd")
    var confirmElement = document.querySelector(".list-share .copy-confirm")
    confirmElement.classList.add("hide"); // reset animation
    void confirmElement.offsetWidth; // trigger reflow
    setTimeout(function(){
    confirmElement.classList.remove("hide"); // start animation
    }, 3000);
  }

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
    <div>
      <div className="dialog-wrap">
        {/* FIXME not the right place, create seperate component */}
      <div className="copy-dialog">
          <span className="share-title">Kopieer lijst</span>
          <span className="share-info">Kopieer de bewaarde aanbiedingen als een boodschappenlijst.</span>
          <div className="list-share">
            <textarea>
            </textarea>
            <span onClick={copyMeTextarea} className="list-copy"><i class="ri-file-copy-2-line"></i><span className='label'>kopieer</span></span>
            <div className="copy-confirm">lijst gekopieerd!</div>
          </div>
        </div>
        <div className="share-dialog">
          <span className="share-title">{buttonText}</span>
          <span className="share-info">{infoText}</span>
          <div className="url-share">
            <input value={shareUrl}/>
            <span onClick={copyMe} className="url-copy"><i class="ri-file-copy-2-line"></i><span className='label'>kopieer</span></span>
            <div className="copy-confirm">link gekopieerd!</div>
          </div>
          <div className="socials">
          <a className="whatsapp" href={"https://api.whatsapp.com/send?text="+shareUrl+""}>
            <i class="ri-whatsapp-fill"></i>
          </a>
          <a className="telegram" href={"https://telegram.me/share/url?url="+shareUrl+"&text="+shareText+""}>
            <i class="ri-telegram-fill"></i>
          </a>
          <a className="twitter" href={"https://twitter.com/intent/tweet?url="+shareUrl+"&text="+shareText+""}>
            <i class="ri-twitter-fill"></i>
          </a>
          <a className="reddit" href={"https://reddit.com/submit?url="+shareUrl+"&title="+shareTitle+""}>
            <i class="ri-reddit-fill"></i>
          </a>
          <a className="linkedin" href={"https://www.linkedin.com/sharing/share-offsite/?url="+shareUrl+""}>
            <i class="ri-linkedin-box-fill"></i>
          </a>
          </div>
        </div>
      </div>
      <div className="button-cell">
        <div onClick={shareApi} className="button share-button">
          <i class="ri-share-box-fill"></i>
          <div className="share-button-tag">{buttonText}</div>
        </div>
      </div>
    </div>
  )

}

export default ShareDialog;
  