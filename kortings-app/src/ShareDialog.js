function ShareDialog(props) {
  
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
          <a className="whatsapp" href="https://api.whatsapp.com/send?text=https://teerkost.nl" >
              <i class="ri-whatsapp-fill"></i>
          </a>
          <a className="telegram" href="https://telegram.me/share/url?url=https://teerkost.nl&text=">
              <i class="ri-telegram-fill"></i>
          </a>
          {/* <a className="twitter" href="">
          <i class="ri-twitter-fill"></i>
          </a>
          <a className="reddit" href="">
              <i class="ri-reddit-fill"></i>
          </a>
          <a className="mail" href="">
              <i class="ri-mail-fill"></i>
          </a>     */}
          </div>
      </div>
      </div>
  )

}

export default ShareDialog;
  