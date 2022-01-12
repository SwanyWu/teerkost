import logo from './logo.svg';
import './App.css';
import Offers from './offers.json';
import Product from './Product';

const expandFilter = () => {
  var dialog = document.getElementById("filter-dialog");
  dialog.classList.toggle('toggle-on');
}

const filter = Offers.filter(object => object.deal === "1+1 gratis")

function App() {

  return (
    <div className="App">
      <div className="filter">
        <div id="filter-dialog">
        <div className="filter-shop">
            <span>Albert Heijn</span>
            <span>Jumbo</span>
          </div>
          <div className="filter-offer">
            <span>1+1 gratis</span>
            <span data-type="offer" data-offer="25% korting">25% korting</span>
            <span>2de halve prijs</span>
          </div>
          <div className="filter-cat">
            <span>Bier</span>
            <span>Wijn</span>
            <span>Brood</span>
          </div>
        </div>
        <div className="filter-button" onClick={expandFilter}>FILTEREN</div>
      </div>
      <div className="info">
        Er zijn 120 Albert Heijn en 115 Jumbo aanbiedingen. 
      </div>
      <div className="flex-container">
      {filter.map(function(name, index){
        return <Product key={index} item={name}/>;
      })}
      </div>
    </div>
  );
}

export default App;
