function Price(props) {

    const price = props.newPrice;

    if(price !== 0) {
        return (
            <span className="product-price">{props.newPrice}</span> 
        )
    }
    else {
        return (<span></span>)
    }
}

export default Price;
  