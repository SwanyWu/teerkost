import React, {useState, useEffect, Suspense} from "react";
import Offers from './offers.json';
import ShareDialog from "./ShareDialog";
import localForage from "localforage";
import NoBookmarks from "./NoBookmarks";
import CopyButton from "./CopyButton";

const ProductsContainer = React.lazy(() => import ('./ProductsContainer'));

function Bookmarks(props) {
  
  useEffect(() => {
    window.scrollTo(0, 0);
  });

  const [selectedOffers, setSelectedOffers] = useState([]);  
  const [bookmarkCount, setBookmarkCount] = useState(0);

  useEffect(() => {
    var bookmarkedIds = undefined;
    localForage.getItem('teerkost-bookmarks').then(function (value) {
      if(value !== null) { // if something is present in browserstorage
        bookmarkedIds = value
        updateOfferListById(bookmarkedIds)
        setBookmarkCount(bookmarkedIds.length)
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
      console.log("Filter voor lijst met bookmarks ingesteld.")
    }
    else {
      console.log("Geen bookmarkId array gevonden, dus niks.")
    }

    console.log("Totale aantal aanbiedingen: " + Offers.length)

    var filtered = Offers.filter(productIdFilter)
    
    setSelectedOffers(filtered);
    console.log("Aantal aanbiedingen na filter: " + filtered.length)
  }

  return (
    <div className="app-wrap">
        <a className="title-sober" href='https://teerkost.nl'><span>Teerkost</span></a>
        { selectedOffers.length > 0  ? 
          <div>
            <div className="bottom-buttons">
              <CopyButton selectedOffers={selectedOffers}/>
              {/* <ShareDialog buttonText="deel lijst" infoText="Deel een link naar deze lijst met bewaarde aanbiedingen." /> */}
            </div>
            <div>
              <header className="filter">
                <div className="filter-wrap">
                  <span className="bookmark-info"><i class="ri-bookmark-line"></i><span>{bookmarkCount} bewaarde aanbieding{bookmarkCount !== 1 ? "en":""}</span></span>
                  <div className="bookmark-options">          
                    {/* <ShareDialog /> */}
                  </div>
                </div>
              </header>
              <Suspense fallback={<div className="even-geduld"><div className="notify-wrap"><span className='dot-dot-dot'></span></div></div>}>
                <ProductsContainer selectedOffers={selectedOffers}/>
              </Suspense>
            </div>
          </div> : <NoBookmarks />
        }
        
    </div>
  )
}

export default Bookmarks;
  