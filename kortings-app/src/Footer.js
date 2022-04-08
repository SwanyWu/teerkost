function Footer() {
    return (
      <footer>
          <a href='https://teerkost.nl'><span className="title">Teerkost</span></a>
          <span className="sub-title-wrap">
            <span className="sub-title">
            Altijd de actuele aanbiedingen van de Albert Heijn, Jumbo, Lidl en Aldi. 
            </span>
          </span>
          <a target="_blank" rel="noreferrer" href="https://www.paypal.com/donate/?business=27RC7XCK9VHH4&no_recurring=0&currency_code=EUR">
            <span className="donate"><i className="wave">👋</i> Dit is een hobbyproject, een <i>donatie</i> is welkom!</span>
          </a>
          <a href="https://github.com/ffyud/teerkost" className="source-link"><i class="ri-github-fill"></i></a>
      </footer>
    )
}

export default Footer;