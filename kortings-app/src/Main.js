import React, {useState, useEffect, Suspense} from "react";
import Offers from './offers.json';

const ProductsContainer = React.lazy(() => import ('./ProductsContainer'));

function Main(props) {
  
  useEffect(() => {
    window.scrollTo(0, 0);
  });

  const [selectedOffers, setSelectedOffers] = useState(Offers);  
  const [selectedShopRoute, setSelectedShopRoute] = useState(props.shop);
  const [selectedDealRoute, setSelectedDealRoute] = useState(props.deal);
  const [selectedCatRoute, setSelectedCatRoute] = useState(props.cat);

  const clickOnShop = (name) => {
    toggleFilterButton(name, "shop")
    if(selectedShopRoute === name) {
      name = undefined
    }
    setSelectedShopRoute(name)
    updateOfferList(name, selectedCatRoute, selectedDealRoute)
  }

  const clickOnCat = (name) => {
    toggleFilterButton(name, "category")
    if(selectedCatRoute === name) {
      name = undefined
    }
    setSelectedCatRoute(name)
    updateOfferList(selectedShopRoute, name, selectedDealRoute)
  }

  const clickOnDeal = (name) => {
    toggleFilterButton(name, "deal")
    if(selectedDealRoute === name) {
      name = undefined
    }
    setSelectedDealRoute(name)
    updateOfferList(selectedShopRoute, selectedCatRoute, name)
  }

  const toggleFilterButton = (name, type) => {
      var htmlIdActive = "active-" + type
      var element = document.querySelectorAll(`[data-${type}="${name}"]`)
      var node = element.item(0)
      if(node != null) {
        if(node.hasAttribute("id")) {
          node.removeAttribute("id") // deactivate the clicked element
        }
        else {
          var activeElement = document.getElementById(htmlIdActive)
          if(activeElement != null) { activeElement.removeAttribute("id")} // deactivate any other element
          
          node.id = htmlIdActive // activate the clicked element
        }
      }
  }

  const updateOfferList = (selectedShopRoute, selectedCatRoute, selectedDealRoute) => {
    var shopFilter = object => object.shop !== null;
    var dealFilter = object => object.deal !== null;
    var categoryFilter = object => object.category !== null;

    if(selectedCatRoute !== undefined) {
      categoryFilter = object => object.category === selectedCatRoute;
      console.log("Filter voor category met " + selectedCatRoute + " ingesteld.")
    }

    if(selectedDealRoute !== undefined) {
      dealFilter = object => object.deal === selectedDealRoute;
      console.log("Filter voor deal met " + selectedDealRoute + " ingesteld.")
    }

    if(selectedShopRoute !== undefined) {
      shopFilter = object => object.shop === selectedShopRoute;
      console.log("Filter voor shop met " + selectedShopRoute + " ingesteld.")
    }
    console.log(Offers.length)

    var filtered = Offers.filter(shopFilter).filter(dealFilter).filter(categoryFilter)
    
    setSelectedOffers(filtered);
    console.log(filtered.length)
  }
        
  return (
    <div>
        <header className="filter"> 
            <div id="filter-dialog">
            <div className="filter-wrap">
                <div className="filter-shop">
                  <span onClick={() => clickOnShop("AH")} data-shop="AH">Albert Heijn</span>
                  <span onClick={() => clickOnShop("Jumbo")}  data-shop="Jumbo">Jumbo</span>
                  <span onClick={() => clickOnShop("Lidl")} data-shop="Lidl">Lidl</span>
                  <span onClick={() => clickOnShop("Aldi")}  data-shop="Aldi">Aldi</span>
                </div>
                <div className="filter-cat">
                  <span onClick={() => clickOnCat("bier")} data-category="bier">Bier</span>
                  <span onClick={() => clickOnCat("koffie")} data-category="koffie">Koffie</span>
                  <span onClick={() => clickOnCat("groente")} data-category="groente">Groente</span>
                  <span onClick={() => clickOnCat("vis")} data-category="vis">Vis</span>
                  <span onClick={() => clickOnCat("fruit")} data-category="fruit">Fruit</span>
                  <span onClick={() => clickOnCat("kant-en-klaar")} data-category="kant-en-klaar">Kant-en-klaar</span>
                  <span onClick={() => clickOnCat("wijn")} data-category="wijn">Wijn</span>
                  <span onClick={() => clickOnCat("aardappel")} data-category="aardappel">Aardappel</span>
                  <span onClick={() => clickOnCat("brood")} data-category="brood">Brood</span>
                  <span onClick={() => clickOnCat("kaas")} data-category="kaas">Kaas</span>
                  <span onClick={() => clickOnCat("noten")} data-category="noten">Noten</span>
                  <span onClick={() => clickOnCat("zuivel")} data-category="zuivel">Zuivel</span>
                  <span onClick={() => clickOnCat("vlees")} data-category="vlees">Vlees</span>
                  <span onClick={() => clickOnCat("verzorging")} data-category="verzorging">Verzorging</span>
                  <span onClick={() => clickOnCat("huishouden")} data-category="huishouden">huishouden</span>
                </div>
                <div className="filter-deal">
                  <span onClick={() => clickOnDeal("1+1 gratis")} data-deal="1+1 gratis">1+1</span>
                  <span onClick={() => clickOnDeal("2+1 gratis")} data-deal="2+1 gratis">2+1</span>
                  <span onClick={() => clickOnDeal("3+1 gratis")} data-deal="3+1 gratis">3+1</span>
                  <span onClick={() => clickOnDeal("10% korting")} data-deal="10% korting">10%</span>
                  <span onClick={() => clickOnDeal("25% korting")} data-deal="25% korting">25%</span>
                  <span onClick={() => clickOnDeal("30% korting")} data-deal="30% korting">30%</span>
                  <span onClick={() => clickOnDeal("40% korting")} data-deal="40% korting">40%</span>
                  <span onClick={() => clickOnDeal("50% korting")} data-deal="50% korting">50%</span>
                  <span onClick={() => clickOnDeal("2e halve prijs")} data-deal="2e halve prijs">2e halve prijs</span>
                  <span onClick={() => clickOnDeal("op=op")} data-deal="op=op">op=op</span>
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
  