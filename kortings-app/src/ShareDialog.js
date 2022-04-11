function ShareDialog(props) {
  
  var shareText = "Altijd de actuele aanbiedingen van de Albert Heijn, Jumbo, Lidl en Aldi."
  var shareUrl = "https://teerkost.nl"

  const copyMe = () => {
    var linkElement = document.querySelector(".url-share input");
    navigator.clipboard.writeText(linkElement.value);
  }
  
  return (
      <div className="share-dialog-wrap">
      <div className="share-dialog">delen
          <span className="title">teerkost</span>
          <span className="share-title">DEEL TEERKOST</span>
          <div className="url-share">
              <input value="https://teerkost.nl"/>
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
          <a className="reddit" href={"https://reddit.com/submit?url="+shareUrl+"&title=Teerkost"}>
              <i class="ri-reddit-fill"></i>
          </a>
          <a className="linkedin" href={"https://www.linkedin.com/sharing/share-offsite/?url="+shareUrl+""}>
            <i class="ri-linkedin-box-fill"></i>
          </a>
          </div>
      </div>
      </div>
  )

}

export default ShareDialog;
  