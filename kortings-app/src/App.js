import React from "react";
import 'remixicon/fonts/remixicon.css'
import './App.css';
import { Routes, Route } from "react-router-dom";
import Footer from './components/Footer';
import Main from './pages/Main';
import Bookmarks from './pages/Bookmarks';
import SingleProduct from './pages/SingleProduct';
import ListProduct from './pages/ListProduct';
import Offers from './offers.json';
import { categoryList } from "./Categories";
import NotFound from "./NotFound";

function App() {
  
  const convertProductToLink = (product) => {
    product = product.trim();
    var parsedProduct = product.normalize('NFD').replace(/[\u0300-\u036f]/g, '') // Remove accents
		.replace(/([^\w]+|\s+)/g, '-') // Replace space and other characters by hyphen
		.replace(/\-\-+/g, '-')	// Replaces multiple hyphens by one hyphen
		.replace(/(^-+|-+$)/g, ''); 
    
    parsedProduct = parsedProduct.toLowerCase(); 

    return parsedProduct;
  }

  const shops = ["jumbo", "aldi", "ah", "lidl", "ekoplaza"]

  return (
    <div className="App">
      <Routes>
        <Route path="/">
          <Route index element={<Main />} />

          {Offers.map((item) => { // Map all routes to the offers
           return <Route path={ "" + item.shop +"/product/" + convertProductToLink(item.product) + ""} element={<SingleProduct item={item} />} />
          })}

          {shops.map((shop, key) => { // Map all routes for shops
            return <Route key={key} path={shop} element={<Main shop={shop} />} />
          })}

          {shops.map((shop) => { // Map all routes for shops and categories
            return categoryList.map((category, key) => {
              return <Route key={key} path={shop + "/" + category} element={<Main shop={shop} cat={category} />} />
            })
          })}

          {categoryList.map((category, key) => { // Map all routes for categories for all shops
              return <Route key={key} path={"alle-winkels/" + category} element={<Main cat={category} />} />
            })}
          
          <Route path="alle-winkels" element={<Main />} /> { /* Map all routes for all shops with everything */ }
          
          <Route path="bewaard" element={<Bookmarks />} />
          <Route path="lijst/:id" element={<ListProduct />} />
          <Route path="*" element={<NotFound/>} />
        </Route>
      </Routes>
      <Footer/>
    </div>
  );
}

export default App;
