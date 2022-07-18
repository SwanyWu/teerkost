function Footer() {
    return (
      <footer>
          <a href='https://teerkost.nl'><span className="title">Teerkost</span></a>
          <span className="sub-title-wrap">
            <span className="sub-title">
            Altijd de actuele aanbiedingen van supermarkten.
            </span>
          </span>
          <a className="donate" target="_blank" rel="noreferrer" href="https://www.paypal.com/donate/?business=27RC7XCK9VHH4&no_recurring=0&currency_code=EUR">
            <span>Dit is een hobbyproject, een <i>donatie</i> is welkom!</span>
          </a>
      </footer>
    )
}

export default Footer;