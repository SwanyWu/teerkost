import logo from './logo.svg';
import './App.css';
import Offers from './offers.json';
import Product from './Product';

function App() {
  return (
    <div className="App">
      <div className="info">Er zijn zoveel aanbiedings</div>
      <div className="flex-container">
      {Offers.map(function(name, index){
        return <Product key={index} item={name}/>;
      })}
      </div>
    </div>
  );
}

export default App;
