function NotFound() {
    return (
      <div className="not-found">
        <a href='https://teerkost.nl'><span className="title">Teerkost</span></a>
        <div className="notify-wrap">
          Deze link bestaat niet.<br/> Probeer wat anders.
          <span className='link-suggest'> 
            <span className='link-wrap'>teerkost.nl/</span>
            <span className='example-wrap'>
              <span className='example-shop'></span>
              <span className='example-cat'></span>
            </span>
        </span>
        </div>
      </div>
    )
}

export default NotFound;
