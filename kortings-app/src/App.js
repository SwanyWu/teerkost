import React, {useState} from "react";
import './App.css';
import Offers from './offers.json';
import Product from './Product';
import NoProduct from "./NoProduct";

const expandFilter = (e) => {
  if(document.getElementById('filter-button').textContent === "FILTER") {
    document.getElementById('filter-button').textContent = "X"
  }
  else {
    document.getElementById('filter-button').textContent = "FILTER"
  }
  var dialog = document.getElementById("filter-dialog");
  dialog.classList.toggle('toggle-on');
}

function App() {
  
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
    
    setFilterDescription(activeShopValue, activeOfferValue, activeCategoryValue)

    setSelectedOffers(filtered);
  }

  const setFilterDescription = (shopValue, offerValue, categoryValue) => {
    var descriptionString = ""
    if(offerValue != null) {
      descriptionString = descriptionString.concat("<b class='label'>" + offerValue + "</b>")
    }
    else {
      descriptionString = descriptionString.concat("<b class='label'>Alle korting</b>")
    }
    if(categoryValue != null) {
      descriptionString = descriptionString.concat("<b class='label'>" + categoryValue + "</b>")
    }
    if(shopValue != null) {
      descriptionString = descriptionString.concat("<b class='label label-shop-"+ shopValue.toLowerCase() +"'>" + shopValue + "</b>")
    }
    else {
      descriptionString = descriptionString.concat("<b class='label label-shop-jumbo'>Jumbo</b><b class='label label-shop-lidl'>Lidl</b><b class='label label-shop-ah'>AH</b>")
    }

    document.getElementById('filter-description').innerHTML = descriptionString
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

  // const searchProducts = (e) => {
  //   setFilterByActiveElements()
  // }

  const [selectedOffers, setSelectedOffers] = useState(Offers);  

  return (
    <div className="App">
      <div className="filter">
        <div id="filter-dialog">
          <div className="filter-wrap">
            <div className="filter-shop">
              <span onClick={filterShop} data-shop="AH">Albert Heijn</span>
              <span onClick={filterShop} data-shop="Jumbo">Jumbo</span>
              <span onClick={filterShop} data-shop="Lidl">Lidl</span>
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
            <div className="filter-cat">
              <span onClick={filterCategory} data-category="bier"><i onClick={(e) => e.stopPropagation()} className="icon">🍺</i> Bier</span>
              <span onClick={filterCategory} data-category="koffie"><i onClick={(e) => e.stopPropagation()} className="icon">☕</i> Koffie</span>
              <span onClick={filterCategory} data-category="groente"><i onClick={(e) => e.stopPropagation()} className="icon">🥬</i> Groente</span>
              <span onClick={filterCategory} data-category="vis"><i onClick={(e) => e.stopPropagation()} className="icon">🐟</i> Vis</span>
              <span onClick={filterCategory} data-category="fruit"><i onClick={(e) => e.stopPropagation()} className="icon">🍓</i> Fruit</span>
              <span onClick={filterCategory} data-category="kant-en-klaar"><i onClick={(e) => e.stopPropagation()} className="icon">🍲</i> Kant-en-klaar</span>
            </div>
            {/* <div className="filter-search"><input id="search" onKeyPress={searchProducts} placeholder="..." type="text"/></div> */}
          </div>
        </div>
      </div>
      <header id="header" onClick={expandFilter}>
      <div id="filter-description">
        <b className="label">Alle korting</b><b className="label label-shop-jumbo">Jumbo</b><b className="label label-shop-lidl">Lidl</b><b className="label label-shop-ah">AH</b>
      </div>
      <div id="filter-button">FILTER</div>
      </header>
      <div className="flex-container">
      { selectedOffers.length > 0 ? selectedOffers.map(function(name, index){
        return <Product key={index} item={name}/>;
      }) : <NoProduct /> }
      </div>
    </div>
  );
}

export default App;
