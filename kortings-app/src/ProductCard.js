import React, {Suspense, useState} from "react";

import DateLabel from './DateLabel';
import Price from './Price';
import Category from './Category';

const Image = React.lazy(() => import ('./Image'));

function ProductCard(props) {

  const [isOpen, setIsOpen] = useState(false);

  // FIXME niet netjes, lostrekken
  const convertProductToLink = (product) => {

    product = product.trim();
  
    const parsedProduct = product.normalize('NFD').replace(/[\u0300-\u036f]/g, '') // Remove accents
    .replace(/([^\w]+|\s+)/g, '-') // Replace space and other characters by hyphen
    .replace(/\-\-+/g, '-')	// Replaces multiple hyphens by one hyphen
    .replace(/(^-+|-+$)/g, ''); 
  
    return parsedProduct;
  }

  const toggleOverlay = () => {
    setIsOpen(isOpen => !isOpen)
  }

    return (
      <article className="flex-item" onClick={toggleOverlay}>
        {isOpen && (
          <div className="item-overlay">
          <ul>
            <li><a href={props.item['link']}>Open op {props.item['shop'] + ".nl"}</a></li>
            <li><a href={"https://teerkost.nl/#/" + props.item['shop'] +"/" + convertProductToLink(props.item['product']) + ""}>Open unieke link</a></li>
          </ul>
        </div>
        )}
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
    )
}

export default ProductCard;
