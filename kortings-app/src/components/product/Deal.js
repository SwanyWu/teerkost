function Deal(props) {

    const dealLabel = props.deal;

    if(dealLabel === '1+1 gratis' || dealLabel === '50% korting') {
      return (
        <span className="product-deal on-fire">
          {dealLabel}
        </span>    
    )
    }
    else {
      return (
        <span className="product-deal">
          {dealLabel}
        </span>    
    )
    }

}

export default Deal;