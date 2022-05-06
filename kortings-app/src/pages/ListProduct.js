import React, {useState, useEffect, Suspense} from "react";
import { useParams } from "react-router-dom";
import Offers from '../offers.json';
import ShareDialog from "../components/ShareDialog";
import BookmarkButton from "../BookmarkButton";
import { categoryList } from "../Categories";
import GoHomeButton from "../GoHomeButton";
import ShareButton from "../ShareButton";

const ProductsContainer = React.lazy(() => import ('../ProductsContainer'));

function Main(props) {
  
  var { id } = useParams();

  const createProductIdsList = (id) => {
    var productIdFilter = object => object.productId === null;

    id = id.split(',')
    console.log(id)
    const aantal = id.length
    console.log(aantal)

    productIdFilter = object => id.includes(object.productId);
    var filtered = Offers.filter(productIdFilter)
    setSelectedOffers(filtered);
  }

  useEffect(() => {
    window.scrollTo(0, 0);
  });

  const updatePageTitle = () => {
    document.title = "gedeelde lijst - Teerkost"
  }

  const [selectedOffers, setSelectedOffers] = useState(Offers);
  const [productIdsList, setProductIdsList] = useState([]);  

  useEffect(() => {
    createProductIdsList(id)
    updatePageTitle()
  }, [])

  return (
    <div className="app-wrap">
        <ShareDialog buttonText="deel lijst" infoText="Deel een link naar deze lijst met aanbiedingen." />
        <div className="bottom-buttons">
          <GoHomeButton />
          <BookmarkButton />
          <ShareButton buttonText="deel lijst" infoText="Deel een link naar deze lijst met aanbiedingen."/>
        </div>
        <a className="title-sober" href='https://teerkost.nl'><span>Teerkost</span></a>
        <header className="filter">
                <div className="filter-wrap">
                  <span className="bookmark-info">
                    Gedeelde lijst
                  </span>
                </div>
              </header>
        <Suspense fallback={<div className="even-geduld"><div className="notify-wrap"><span className='dot-dot-dot'></span></div></div>}>
            <ProductsContainer selectedOffers={selectedOffers}/>
        </Suspense>
    </div>
  )
}

export default Main;
  