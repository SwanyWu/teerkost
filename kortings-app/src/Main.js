import React, {useState, useEffect, Suspense} from "react";
import Offers from './offers.json';

const ProductsContainer = React.lazy(() => import ('./ProductsContainer'));

function Main(props) {
   
  useEffect(() => {
    window.scrollTo(0, 0);
  });

  const toggleFilterClass = (clickedElement, type) => {
        if(type === 'offer') {
          var otherElementOffer = document.getElementById('active-offer')
          if(otherElementOffer !== null) { 
            if(otherElementOffer === clickedElement) {
              clickedElement.removeAttribute("id")
            }
            else {
              otherElementOffer.removeAttribute("id") 
              clickedElement.id = 'active-offer'
            }
          }
          else {
            clickedElement.id = 'active-offer'
          }
        }
        else if(type === 'shop') {
          var otherElementShop = document.getElementById('active-shop')
          if(otherElementShop !== null) { 
            if(otherElementShop === clickedElement) {
              clickedElement.removeAttribute("id")
            }
            else {
              otherElementShop.removeAttribute("id") 
              clickedElement.id = 'active-shop'
            }
          }
          else {
            clickedElement.id = 'active-shop'
          }
        }
        else if(type === 'category') {
          var otherElementCategory = document.getElementById('active-category')
          if(otherElementCategory !== null) { 
            if(otherElementCategory === clickedElement) {
              clickedElement.removeAttribute("id")
            }
            else {
              otherElementCategory.removeAttribute("id") 
              clickedElement.id = 'active-category'
            }
          }
          else {
            clickedElement.id = 'active-category'
          }
        }
      }
    
      const setFilterByActiveElements = () => {
        var activeShop = document.getElementById("active-shop");
        var activeOffer = document.getElementById("active-offer");
        var activeCategory = document.getElementById("active-category");
    
        var shopFilter = object => object.shop !== null;
        var offerFilter = object => object.deal !== null;
        var categoryFilter = object => object.category !== null;
    
        if(activeShop !== null) { 
          var activeShopValue = activeShop.getAttribute('data-shop');
          shopFilter = object => object.shop === activeShopValue;
        }
        if(activeOffer !== null) {
          var activeOfferValue = activeOffer.getAttribute('data-offer');
          offerFilter = object => object.deal === activeOfferValue;
        }
        if(activeCategory !== null) {
          var activeCategoryValue = activeCategory.getAttribute('data-category');
          categoryFilter = object => object.category === activeCategoryValue;
        }
    
        var filtered = Offers.filter(shopFilter).filter(offerFilter).filter(categoryFilter)
        
        setSelectedOffers(filtered);
    
      }
    
      const filterOffer = (e) => {
        toggleFilterClass(e.target, "offer")
        setFilterByActiveElements()
      }
    
      const filterShop = (e) => {
        toggleFilterClass(e.target, "shop")
        setFilterByActiveElements()
      }
    
      const filterCategory = (e) => {
        toggleFilterClass(e.target, "category")
        setFilterByActiveElements()
      }
    
      const [selectedOffers, setSelectedOffers] = useState(Offers);  
    
      return (
        <div>
            <header className="filter"> 
                <div id="filter-dialog">
                <div className="filter-wrap">
                    <div className="filter-shop">
                    <span onClick={filterShop} data-shop="AH">Albert Heijn</span>
                    <span onClick={filterShop} data-shop="Jumbo">Jumbo</span>
                    <span onClick={filterShop} data-shop="Lidl">Lidl</span>
                    </div>
                    <div className="filter-cat">
                    <span onClick={filterCategory} data-category="bier"><i onClick={(e) => e.stopPropagation()} className="icon">🍺</i> Bier</span>
                    <span onClick={filterCategory} data-category="koffie"><i onClick={(e) => e.stopPropagation()} className="icon">☕</i> Koffie</span>
                    <span onClick={filterCategory} data-category="groente"><i onClick={(e) => e.stopPropagation()} className="icon">🥬</i> Groente</span>
                    <span onClick={filterCategory} data-category="vis"><i onClick={(e) => e.stopPropagation()} className="icon">🐟</i> Vis</span>
                    <span onClick={filterCategory} data-category="fruit"><i onClick={(e) => e.stopPropagation()} className="icon">🍓</i> Fruit</span>
                    <span onClick={filterCategory} data-category="kant-en-klaar"><i onClick={(e) => e.stopPropagation()} className="icon">🍲</i> Kant-en-klaar</span>
                    <span onClick={filterCategory} data-category="aardappel"><i onClick={(e) => e.stopPropagation()} className="icon">🥔</i> Aardappel</span>
                    <span onClick={filterCategory} data-category="brood"><i onClick={(e) => e.stopPropagation()} className="icon">🍞</i> Brood</span>
                    <span onClick={filterCategory} data-category="kaas"><i onClick={(e) => e.stopPropagation()} className="icon">🧀</i> Kaas</span>
                    <span onClick={filterCategory} data-category="noten"><i onClick={(e) => e.stopPropagation()} className="icon">🥜</i> Noten</span>
                    <span onClick={filterCategory} data-category="verzorging"><i onClick={(e) => e.stopPropagation()} className="icon">🛁</i> Verzorging</span>
                    <span onClick={filterCategory} data-category="huishoudelijk"><i onClick={(e) => e.stopPropagation()} className="icon">🧽</i> Huishoudelijk</span>

                    </div>
                    <div className="filter-offer">
                    <span onClick={filterOffer} data-offer="1+1 gratis">1+1</span>
                    <span onClick={filterOffer} data-offer="2+1 gratis">2+1</span>
                    <span onClick={filterOffer} data-offer="3+1 gratis">3+1</span>
                    <span onClick={filterOffer} data-offer="10% korting">10%</span>
                    <span onClick={filterOffer} data-offer="25% korting">25%</span>
                    <span onClick={filterOffer} data-offer="30% korting">30%</span>
                    <span onClick={filterOffer} data-offer="40% korting">40%</span>
                    <span onClick={filterOffer} data-offer="50% korting">50%</span>
                    <span onClick={filterOffer} data-offer="2e halve prijs">2e halve prijs</span>
                    </div>
                </div>
                </div>
            </header>
            <Suspense fallback={<div className="even-geduld">Even geduld...</div>}>
                <ProductsContainer selectedOffers={selectedOffers}/>
            </Suspense>
        </div>
      )

}

export default Main;
  