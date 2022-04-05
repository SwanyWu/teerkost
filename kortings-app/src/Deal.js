function Deal(props) {

    const dealLabel = props.deal;

    return (
        <span className="product-deal">
          {dealLabel}
        </span>    
    )
}

export default Deal;