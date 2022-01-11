import logo from './logo.svg';
import './App.css';
import Offers from './offers.json';
import Product from './Product';


function App() {

  // const aantalAh = Offers.filter().length;

  return (
    <div className="App">
      <div className="filter-button">FILTEREN</div>
      <div className="info">
        Er zijn 120 Albert Heijn en 115 Jumbo aanbieding. 
      </div>
      <div className="flex-container">
      {Offers.map(function(name, index){
        return <Product key={index} item={name}/>;
      })}
      </div>
    </div>
  );
}

export default App;
