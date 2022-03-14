import React, {useEffect} from "react";
import './App.css';
import { BrowserRouter, Routes, Route, Link, useNavigate } from "react-router-dom";
import Footer from './Footer';
import Main from './Main';
import SingleProduct from './SingleProduct';
import Counter from './Counter';


function App() {
  
  useEffect(() => {
    window.scrollTo(0, 0);
  });

  const name = {
    "product": "Excellent vleeswaren",
    "productInfo": "Bijv. Spianata romana - Per stuk",
    "category": "",
    "image": "https://static.ah.nl/static/product/AHI_43545239373737313836_1_200x200_JPG.JPG",
    "deal": "3 voor 5.00",
    "price": 5,
    "dateStart": "2022-03-14",
    "dateEnd": "2022-03-20",
    "link": "https://ah.nl/bonus/groep/348290?week=11",
    "shop": "AH"
  }

  return (
    <div className="App">
      <Routes>
        <Route path="/excellent-vleeswaren" element={<SingleProduct item={name} />} />
        <Route path="/" element={<Main />}/>
      </Routes>

              {/* <Counter selectedOffers={5} totalOffers={10}/> */}

      <h1 className="page-title">Teerkost</h1>
      
      <Footer/>
    </div>
  );
}

export default App;
