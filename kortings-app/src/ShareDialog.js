function ShareDialog(props) {
  
  var shareText = "Altijd de actuele aanbiedingen van supermarkten."
  var shareUrl = window.location.href
  var shareTitle = document.title

  const copyMe = () => {
    var linkElement = document.querySelector(".url-share input");
    navigator.clipboard.writeText(linkElement.value);
  }

  const shareApi = (e) => {
    if (navigator.share) {
      navigator.share({
        title: shareTitle,
        url: shareUrl
      }).then(() => {
        console.log('Dankje');
      })
      .catch(console.error);
    } else {
      var shareButtonElement = document.querySelector('.share-button')
      var shareDialogElement = document.querySelector('.share-dialog')
      var wrapElement = document.querySelector('.share-dialog-wrap')

      var clickOutside = function(e) {
        if ( !shareDialogElement.contains(e.target) && !shareButtonElement.contains(e.target)) {
          wrapElement.removeAttribute("id") 
          if(!wrapElement.hasAttribute("id")) { // stop listening to clicks outside the dialog
            return document.removeEventListener('click', clickOutside)
          }
        }
      }  

      if(! wrapElement.hasAttribute("id")) {
        wrapElement.id = "dialog-on"
        if(wrapElement.id === "dialog-on") { // listen to clicks outside the dialog
          document.addEventListener('click', clickOutside) 
        }   
      }
    }
  }

  return (
    <div>
      <div className="share-dialog-wrap">
        <div className="share-dialog">delen
          <span className="title">teerkost</span>
          <span className="share-title">DEEL TEERKOST</span>
          <div className="url-share">
            <input value={shareUrl}/>
            <span onClick={copyMe} className="url-copy">kopieer</span>
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
        </div>
      </div>
    </div>
  )

}

export default ShareDialog;
  