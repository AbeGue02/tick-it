export default function SearchBar({searchBarText, setSearchBarText, onSubmit}) {
    return (
        <div className="searchBarContainer">
            <input 
                type="text"
                value={searchBarText}
                onChange={(e) => setSearchBarText(e.target.value)}
                placeholder="Search..."/>
            <button onClick={onSubmit}>Submit</button>
        </div>
    )
}