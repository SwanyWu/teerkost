import localForage from 'localforage'

function ProductBookmark(props) {

    const productId = props.id;

    const triggerButtonAnimation = () => {

        const element = document.querySelector('.personal-list-button')
        if(element !== null) {
            element.classList.remove('jumpy'); // reset animation
            void element.offsetWidth; // trigger reflow
            element.classList.add('jumpy'); // start animation
        }
    }

    const triggerButtonUpdate = () => {
        localForage.getItem('teerkost-bookmarks').then(function (value) {
            var amount = 0
            if(value !== null) {
                amount = value.length
            }
            const element = document.querySelector('.personal-list-button-tag')
            if(element !== null) {
                element.textContent = amount    
            }
        }) 
    }

    const registerBookmark = (id) => {
        localForage.getItem('teerkost-bookmarks').then(function (value) {
            if(value !== null) { // if something is present in browserstorage
                const valueFound = value.find(element => element === id)

                if(valueFound === id) {
                    var allBookmarks = value;
                    allBookmarks = allBookmarks.filter(element => element !== id) // remove from existing array
                    console.log(id + " wordt verwijdert aan de bookmarks.")

                    localForage.setItem('teerkost-bookmarks', allBookmarks).then(function(value) {
                        triggerButtonAnimation()
                        triggerButtonUpdate()
                    }).catch(function (err) {
                        console.log("Iets misgegaan bij het opslaan van bookmarks: " + err)
                    })
                } else {
                    var allBookmarks = value;
                    allBookmarks.push(id) // push to the existing array
                    console.log(id + " wordt toegevoegt aan de bookmarks.")
                    localForage.setItem('teerkost-bookmarks', allBookmarks).then(function(value) {
                        triggerButtonAnimation()
                        triggerButtonUpdate()
                    }).catch(function (err) {
                        console.log("Iets misgegaan bij het opslaan van bookmarks: " + err)
                    })
                }
            } else {
                var allBookmarks = [id] // nothing found, make a new array with first id
                console.log("niks gevonden. Tijd om te starten")
                localForage.setItem('teerkost-bookmarks', allBookmarks).then(function(value) {
                    console.log("Voor het eerst, de array " + value + " toegevoegd")
                }).catch(function (err) {
                    console.log("Iets misgegaan bij het opslaan van eerste bookmark: " + err)
                })
            }
        }).catch(function(err) {
            console.log("Iets misgegaan bij het ophalen van data: " + err)
        })
    }

    const getCorrectBookmarkIcon = (productId) => {
        localForage.getItem('teerkost-bookmarks').then(function (value) {
            if(value !== null) { // if something is present in browserstorage
                const valueFound = value.find(element => element === productId)
                if(valueFound === productId) {
                    return "ja"
                    // return <i class='ri-bookmark-line'></i>
                } else {
                    return "nee"
                }
            } else {
                return "aaaa"
            }
        })
        return <i class='ri-bookmark-line'></i>
    }

    return (
        <span onClick={() => registerBookmark(productId)} className="product-bookmark">{getCorrectBookmarkIcon(productId)}</span>
    )

}

export default ProductBookmark;