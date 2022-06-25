import React, {useState, useEffect} from "react";
import NoProduct from "./pages/NoProduct";
import ProductCard from "./components/ProductCard";

function ProductsContainer(props) {

    const [totalLength, setTotalLength] = useState(props.selectedOffers.length)
    const [listLength, setListLength] = useState(100)

    useEffect(() => {
      setTotalLength(props.selectedOffers.length)
    })

    const setNewLimit = () => {
      setListLength(listLength + 100)
    }

    return (
        <main className="flex-container">
        { totalLength > 0 ? props.selectedOffers.slice(0,listLength).map(function(name, index){
          return <ProductCard key={index} item={name}/>;
        }) : <NoProduct /> }
        { totalLength > 100 && listLength < totalLength ? 
          <div onClick={setNewLimit} className="show-more">
          <span>Toon meer</span></div> : <div></div>}
        </main>
    )
}

export default ProductsContainer;