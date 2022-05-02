import React, {useState, useEffect, Suspense} from "react";
import Offers from '../offers.json';
import ShareDialog from "../components/ShareDialog";
import BookmarkButton from "../BookmarkButton";
import { categoryList } from "../Categories";

const ProductsContainer = React.lazy(() => import ('../ProductsContainer'));

function Main(props) {
  
  const categories = []
  categoryList.forEach(element => {
    categories.push([element, 0]) // for filling the filters on screen
  })

  let shops = [
    ['ah', 0], ['jumbo', 0], ['lidl', 0], ['aldi', 0], ['plus', 0], ['ekoplaza', 0]
  ]

  const [categoriesList, setCategoriesList] = useState(categories)
  const [shopsList, setShopsList] = useState(shops)

  useEffect(() => {
    window.scrollTo(0, 0);
  });

  const [selectedOffers, setSelectedOffers] = useState(Offers);  
  const [selectedShopRoute, setSelectedShopRoute] = useState(props.shop);
  const [selectedDealRoute, setSelectedDealRoute] = useState(props.deal);
  const [selectedCatRoute, setSelectedCatRoute] = useState(props.cat);

  useEffect(() => {
    toggleFilterButton(selectedShopRoute, "shop")
    toggleFilterButton(selectedCatRoute, "category")
    toggleFilterButton(selectedDealRoute, "deal")

    setCounterPerCategory(selectedShopRoute)
    setCounterPerShop()

    updateOfferList(selectedShopRoute, selectedCatRoute, selectedDealRoute)
    updatePageTitle(selectedShopRoute, selectedCatRoute)

    setFilterNotStickyOnSmallScreen()

  }, [])

  const setFilterNotStickyOnSmallScreen = () => {
    var checkSticky = () => {
      var filterWrapElement = document.querySelector(".filter");
      var minHeight = 900 // hardcoded because height of element is not known on mount
      var heightWindow = window.innerHeight
        if(heightWindow < minHeight ) {
        filterWrapElement.classList.add('not-sticky') // make it not sticky
      } else {
        filterWrapElement.classList.remove('not-sticky') // make it sticky
      }
    }

    // on load 
    checkSticky()
    // and on resize
    window.onresize = () => { checkSticky() };
  }


  const setCounterPerShop = () => {
    let tempList = []
    shopsList.map((shop, key) => {
      var shopFilter = object => object.shop === shop[0];

      var filterByShop = Offers.filter(shopFilter)
      var numberCountByShop = filterByShop.length

      let shopObjectTemp = [shop[0], numberCountByShop]
      return tempList.push(shopObjectTemp)
    })
    setShopsList(tempList)
  }

  const setCounterPerCategory = (shop) => {
    if(shop !== undefined) {
      var shopFilter = object => object.shop === shop;

    }
    else {
      var shopFilter = object => object.shop !== null;
    }
  
    let tempList = []
    categoriesList.map((category, key) => {
      var categoryFilter = object => object.category === category[0];

      var filterByCategory = Offers.filter(shopFilter).filter(categoryFilter)
      var numberCountByCategory = filterByCategory.length

      let categoryObjectTemp = [category[0], numberCountByCategory]
      return tempList.push(categoryObjectTemp)
    })
    setCategoriesList(tempList)
  }

  const updateUrl = (shopName, catName) => {
    var shopUrlPart = ""
    var catUrlPart = ""
    if(shopName !== undefined) {
      shopUrlPart = "/#/" + shopName;
    } else {
      shopUrlPart = "/#/alle-winkels"
    }
    if(catName !== undefined) {
      if(shopName === undefined) {
        shopUrlPart = "/#/alle-winkels"
      }
      catUrlPart = "/" + catName;
    }
    window.history.pushState({}, '', shopUrlPart + catUrlPart);
    updatePageTitle(shopName, catName)
  }

  const updatePageTitle = (shopName, catName) => {
    var shopPart = ""
    var catPart = ""
    var titlePart = "Teerkost"
    if(shopName !== undefined) {
      shopPart = " " + shopName + " - ";
    }
    if(catName !== undefined) {
      if(shopName === undefined) {
        shopPart = " "
      }
      catPart = catName + " - ";
    }
    if(shopName !== undefined || catName !== undefined) {
      titlePart = "Teerkost"
    } 
    document.title = catPart + "" + shopPart + titlePart 
  }

  const clickOnShop = (name) => {
    toggleFilterButton(name, "shop")
    if(selectedShopRoute === name) {
      name = undefined
    }
    setSelectedShopRoute(name)
    setCounterPerCategory(name)
    updateOfferList(name, selectedCatRoute, selectedDealRoute)
    updateUrl(name, selectedCatRoute)
  }

  const clickOnCat = (name) => {
    toggleFilterButton(name, "category")
    if(selectedCatRoute === name) {
      name = undefined
    }
    setSelectedCatRoute(name)
    updateOfferList(selectedShopRoute, name, selectedDealRoute)
    updateUrl(selectedShopRoute, name)
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
    console.log("Totale aantal aanbiedingen: " + Offers.length)

    categoryList.push('') // for offers without a category
    Offers.sort(function(a, b){  // sorting according to categorySorting array
        return categoryList.indexOf(a.category) - categoryList.indexOf(b.category);
    });

    var filtered = Offers.filter(shopFilter).filter(dealFilter).filter(categoryFilter)
    
    setSelectedOffers(filtered);
    console.log("Aantal aanbiedingen na filter: " + filtered.length)
  }

  return (
    <div className="app-wrap">
        <div className="bottom-buttons">
          <BookmarkButton />
          <ShareDialog buttonText="deel pagina" infoText="Deel de huidige pagina met de gekozen filters." />
        </div>
        <a className="title-sober" href='https://teerkost.nl'><span>Teerkost</span></a>
        <header className="filter">
            <div id="filter-dialog">
            <div className="filter-wrap">
                <div className="filter-shop">
                  {shopsList.map((shop, key) => {
                    return <span onClick={() => clickOnShop(shop[0])} data-shop={shop[0]}>{shop[0]} <i className="counter">{shop[1]}</i></span>
                  })}
                </div>
                <div className="filter-cat">
                  {categoriesList.map((category, key) => {
                    if(category[0] !== "") { // don't show empty filters
                      if(category[1] === 0) {
                        return <span className='filter-no-interest' key={key} onClick={() => clickOnCat(category[0])} data-category={category[0]}>{category[0]}</span>
                      }
                      else {
                        return <span key={key} onClick={() => clickOnCat(category[0])} data-category={category[0]}>{category[0]} <i className="counter" data-category="bier">{category[1]}</i></span>
                      }
                    }
                    else { return ""}
                    
                  })}
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
        <Suspense fallback={<div className="even-geduld"><div className="notify-wrap"><span className='dot-dot-dot'></span></div></div>}>
            <ProductsContainer selectedOffers={selectedOffers}/>
        </Suspense>
    </div>
  )
}

export default Main;
  