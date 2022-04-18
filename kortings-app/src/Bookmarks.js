import React, {useState, useEffect, Suspense} from "react";
import Offers from './offers.json';
import ShareDialog from "./ShareDialog";
import localForage from "localforage";
import NoBookmarks from "./NoBookmarks";

const ProductsContainer = React.lazy(() => import ('./ProductsContainer'));

function Bookmarks(props) {
  
  useEffect(() => {
    window.scrollTo(0, 0);
  });

  const [selectedOffers, setSelectedOffers] = useState([]);  

  useEffect(() => {

    var bookmarkedIds = undefined;
    localForage.getItem('teerkost-bookmarks').then(function (value) {
      if(value !== null) { // if something is present in browserstorage
        bookmarkedIds = value
        updateOfferListById(bookmarkedIds)
      } else {
        console.info("Er staan geen bookmarks in deze browser opgeslagen.")
      }
    }).catch(function(err) {
        console.warn("Iets misgegaan bij het ophalen van de bookmarks: " + err)
    })
  }, [])

  const updateOfferListById = (bookmarkIdList) => {

    var productIdFilter = object => object.productId === null;

    if(bookmarkIdList !== null) {
      productIdFilter = object => bookmarkIdList.includes(object.productId);
      console.log("Filter voor categorie met " + bookmarkIdList + " ingesteld.")
    }
    else {
      console.log("Geen bookmarkId array gevonden, dus niks.")
    }

    console.log("Totale aantal aanbiedingen: " + Offers.length)

    var filtered = Offers.filter(productIdFilter)
    
    setSelectedOffers(filtered);
    console.log("Aantal aanbiedingen na filter: " + filtered.length)
  }

  const aantalBookmarks = () => {
    var aantal = 0
    localForage.getItem("teerkost-bookmarks").then(function(value) {
      if(value !== null) {
        aantal = value.length
        console.log("Er zijn " + aantal+ " bookmarks gevonden in de opslag.")
      }
    }).catch(function(err) {
      console.warn("Er is wat misgegaan bij het ophalen van de bookmarks: " + err)
     })

    return aantal
  }
  return (
    <div className="app-wrap">
        <div className="bottom-buttons">
          {/* <div className="button-cell">
            <div className="button personal-list-button">
              <i class="ri-bookmark-line"></i>
            </div>
          </div> */}
        </div>
        { selectedOffers.length > 0  ? 
          <div>
            <header className="filter">
              <a className="title-sober" href='https://teerkost.nl'><span>Teerkost</span></a>
              <div className="filter-wrap">
                <span className="bookmark-info">{aantalBookmarks()} bewaarde aanbiedingen.</span>
                <div className="bookmark-options">          
                  <ShareDialog />
                  <span className="button bookmark-copy">
                    <i class="ri-file-copy-2-line"></i>
                    <div className="bookmark-copy-tag">kopieer boodschappenlijst</div>
                  </span>
                </div>
              </div>
            </header>
            <Suspense fallback={<div className="even-geduld"><div className="notify-wrap"><span className='dot-dot-dot'></span></div></div>}>
              <ProductsContainer selectedOffers={selectedOffers}/>
            </Suspense>
          </div> : <NoBookmarks />
        }
        
    </div>
  )
}

export default Bookmarks;
  