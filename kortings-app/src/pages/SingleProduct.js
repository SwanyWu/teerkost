import React, {Suspense, useEffect} from "react";

import DateLabel from '../components/product/DateLabel';
import Price from '../components/product/Price';
import Category from '../components/product/Category';
import Deal from '../components/product/Deal';
import ShareDialog from "../components/ShareDialog";
import ProductBookmark from "../components/product/ProductBookmark";
import BookmarkButton from "../BookmarkButton";

const Image = React.lazy(() => import ('../components/product/Image'));

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
          <div className={"product-header " + props.item['shop']}>
            <span className="product-shop">{props.item['shop']}</span>
            <DateLabel dateEnd={props.item['dateEnd']} dateStart={props.item['dateStart']}/>
          </div>
          <Category category={props.item['category']}/>
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
