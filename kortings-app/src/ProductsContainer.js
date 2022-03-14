import NoProduct from "./NoProduct";
import ProductCard from "./ProductCard";

function ProductsContainer(props) {
    return (
        <main className="flex-container">
        { props.selectedOffers.length > 0 ? props.selectedOffers.map(function(name, index){
          return <ProductCard key={index} item={name}/>;
        }) : <NoProduct /> }
        </main>
    )
}

export default ProductsContainer;