import React, {Suspense, useEffect} from "react";

import DateLabel from './DateLabel';
import Price from './Price';
import Category from './Category';
import Deal from './Deal';
import ShareDialog from "./ShareDialog";
import ProductBookmark from "./ProductBookmark";
import BookmarkButton from "./BookmarkButton";

const Image = React.lazy(() => import ('./Image'));

function SingleProduct(props) {

  useEffect(() => {
    window.scrollTo(0, 0);
  });

    return (
      <div className="app-wrap">
        <div className="bottom-buttons">
          <BookmarkButton />
          <ShareDialog />
        </div>
        <a className="title-sober" href='https://teerkost.nl'><span>Teerkost</span></a>
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
          <Deal deal={props.item['deal']} />
          <ProductBookmark id={props.item['productId']}/>
        </article>
        </div>
      </div>

    )
}

export default SingleProduct;
