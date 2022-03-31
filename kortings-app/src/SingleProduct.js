import React, {Suspense, useEffect} from "react";

import DateLabel from './DateLabel';
import Price from './Price';
import Category from './Category';

const Image = React.lazy(() => import ('./Image'));

function SingleProduct(props) {

  useEffect(() => {
    window.scrollTo(0, 0);
  });

    return (
      <div className="container">
      <article className="single-item">
        <span className={"product-shop " + props.item['shop']}>{props.item['shop']}</span>
        <Category category={props.item['category']}/>
        <DateLabel dateEnd={props.item['dateEnd']} dateStart={props.item['dateStart']}/>
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
      </div>
    )
}

export default SingleProduct;
