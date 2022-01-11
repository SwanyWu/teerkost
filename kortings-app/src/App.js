import logo from './logo.svg';
import './App.css';
import offerAh from './offer-ah.json';
import offerJumbo from './offer-jumbo.json';
import Product from './Product';

function App() {
  return (
    <div className="App">
      <div className="info">Er zijn zoveel aanbiedings</div>
      <div className="flex-container">
      {offerAh.map(function(name, index){
        return <Product key={index} item={name}/>;
      })}
      </div>
    </div>
  );
}

export default App;
