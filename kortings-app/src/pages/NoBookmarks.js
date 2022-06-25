import ShareDialog from "../components/ShareDialog";
import GoHomeButton from "../GoHomeButton";
import BookmarkButton from "../BookmarkButton";
import ShareButton from "../ShareButton";
import SearchButton from "../SearchButton";

function NoBookmarks() {
    return (
      <div className="app-wrap">
        <ShareDialog customUrl="https://teerkost.nl/#/bewaard" buttonText="deel pagina" infoText="Deel de huidige pagina." />
        <div className="bottom-buttons">
          <GoHomeButton />
          <SearchButton />
          <BookmarkButton />
          <ShareButton customUrl="https://teerkost.nl/#/bewaard" buttonText="deel" infoText="Deel de huidige pagina."/>
        </div>
        <div className="no-offers">
          <div className='notify-wrap'>
            Geen bewaarde korting gevonden
          </div>
          <div className='notify-explainer'>
            Voeg ze toe door op <i class="ri-bookmark-line"></i> te klikken bij een korting.
          </div>
        </div>
      </div>
    )
}

export default NoBookmarks;
