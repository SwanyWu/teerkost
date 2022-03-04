import NoProduct from "./NoProduct";
import Product from "./Product";

function ProductsContainer(props) {
    return (
        <div className="flex-container">
        { props.selectedOffers.length > 0 ? props.selectedOffers.map(function(name, index){
          return <Product key={index} item={name}/>;
        }) : <NoProduct /> }
        </div>
    )
}

export default ProductsContainer;