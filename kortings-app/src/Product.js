function Product(props) {
  if(props.item['shop'] === 'AH') {
    return (
      <div className="flex-item shop-ah">
        <span className="product-image"><img alt={props.item['product']} src={props.item['image']}/></span>
        <span className="product-name">
          {props.item['product']}
          <span className="product-info"> {props.item['productInfo']}</span>
        </span>
        <span className='product-date-end'>{props.item['dateEnd']}</span>
        <span className="product-price">{props.item['price']}</span>   
        <span className="product-deal">{props.item['deal']}</span>
      </div>
    )
  }
  else
    return (
      <div className="flex-item shop-jumbo">
        <span className="product-image"><img alt={props.item['product']} src={props.item['image']}/></span>
        <span className="product-name">
          {props.item['product']}
          <span className="product-info"> {props.item['productInfo']}</span>
        </span>
        <span className='product-date-end'>{props.item['dateEnd']}</span>
        <span className="product-price">{props.item['price']}</span> 
        <span className="product-deal">{props.item['deal']}</span>
      </div>
    )
}

export default Product;
