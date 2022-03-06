import Date from './Date';
import Price from './Price';

function Product(props) {
    return (
      <article className="flex-item">
        <span className={"product-shop " + props.item['shop']}>{props.item['shop']}</span>
        <Date dateEnd={props.item['dateEnd']} dateStart={props.item['dateStart']}/>
        <Price newPrice={props.item['price']} />
        <span className="product-image"><img alt={props.item['product']} src={props.item['image']}/></span>
        <summary className="product-name">
          {props.item['product']}
          <span className="product-info"> {props.item['productInfo']}</span>
        </summary>
        <span className="product-deal">
          {props.item['deal']}
        </span>
      </article>
    )
}

export default Product;
