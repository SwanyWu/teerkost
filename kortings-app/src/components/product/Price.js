function Price(props) {

    const price = props.newPrice;

    if(price !== 0 && price !== "0" && price !== "") {
        return (
            <span className="product-price">{price}</span> 
        )
    }
    else {
        return (<span></span>)
    }
}

export default Price;
  