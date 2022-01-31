import Date from './Date';
import Price from './Price';

function Product(props) {
    return (
      <div className="flex-item">
        <span className="product-image"><img alt={props.item['product']} src={props.item['image']}/></span>
        <span className="product-name">
          {props.item['product']}
          <span className="product-info"> {props.item['productInfo']}</span>
        </span>
        <span className={"product-shop " + props.item['shop']}>{props.item['shop']}</span>
        <Date dateEnd={props.item['dateEnd']} />
        <Price newPrice={props.item['price']} />
        <span className="product-deal">{props.item['deal']}</span>
      </div>
    )
}

export default Product;
