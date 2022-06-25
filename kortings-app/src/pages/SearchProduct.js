import React, {useState, useEffect, Suspense} from "react";
import { useParams } from "react-router-dom";
import Offers from '../offers.json';
import ShareDialog from "../components/ShareDialog";
import BookmarkButton from "../BookmarkButton";
import GoHomeButton from "../GoHomeButton";
import ShareButton from "../ShareButton";
import SearchButton from "../SearchButton";

const ProductsContainer = React.lazy(() => import ('../ProductsContainer'));

function SearchProduct(props) {
  
  useEffect(() => {
    window.scrollTo(0, 0);
  });

  const updatePageTitle = () => {
    document.title = "zoeken - Teerkost"
  }
  
  const setSearchFilter = (searchValue) => {
    let offersBySearch = Offers.filter(
      object => object.product.toLowerCase().includes(searchValue.toLowerCase()) || 
                object.productInfo.toLowerCase().includes(searchValue.toLowerCase()) || 
                object.category.toLowerCase().includes(searchValue.toLowerCase()));
    setSelectedOffers(offersBySearch)
  }

  const handleKeyPress = (e) => {
    console.log( e.target.value)
    setSearchFilter(e.target.value)

  }

  const [selectedOffers, setSelectedOffers] = useState(Offers);

  useEffect(() => {
    updatePageTitle()
        // setSearchFilter()

  }, [selectedOffers])

  return (
    <div className="app-wrap">
        <ShareDialog buttonText="deel pagina" infoText="Deel een link naar deze pagina." />
        <div className="bottom-buttons">
          <GoHomeButton />
          <SearchButton />
          <BookmarkButton />
          <ShareButton buttonText="deel" infoText="Deel een link naar deze pagina."/>
        </div>
        <a className="title-sober" href='https://teerkost.nl'><span>Teerkost</span></a>
          <header className="header-title">
            <input onChange={(e) => handleKeyPress(e)} className="filter-search" type="text" placeholder="Zoek een aanbieding..." autoFocus></input>
          </header>
        <Suspense fallback={<div className="even-geduld"><div className="notify-wrap"><span className='dot-dot-dot'></span></div></div>}>
            <ProductsContainer selectedOffers={selectedOffers}/>
        </Suspense>
    </div>
  )
}

export default SearchProduct;
  