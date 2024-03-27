export default function VenueListItem (props) {
    
    return (
        <div className='venueListItemContainer'>
                <h3>{props.venue.name}</h3>
                <h4>{props.venue.location}</h4>
        </div>
       
       
    )
}