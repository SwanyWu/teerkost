import React, {Suspense, lazy} from "react";

import Date from './Date';
import Price from './Price';

const Image = React.lazy(() => import ('./Image'));

function Product(props) {
    return (
      <article className="flex-item">
        <span className={"product-shop " + props.item['shop']}>{props.item['shop']}</span>
        <Date dateEnd={props.item['dateEnd']} dateStart={props.item['dateStart']}/>
        <Price newPrice={props.item['price']} />
        <Suspense fallback={<div className="even-geduld-image"></div>}>
          <Image image={props.item['image']} />
        </Suspense> 
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
