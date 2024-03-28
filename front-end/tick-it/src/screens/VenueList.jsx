import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'
import SearchBar from '../components/SearchBar'
import VenueListItem from '../components/VenueListItem'

export default function VenueList() {
    const [venues, setVenues] = useState([])
    const { venueId } = useParams()
    const [events, setEvents] = useState([])
    const [searchBarText, setSearchBarText] = useState('')

    // const fetchVenues = async () => {
    //     let response = await axios.get('http://localhost:8000/venues')
    //     setVenues(response.data)
    // }

    // useEffect(() => {
    //     fetchVenues()
    // }, [])

    const getVenues = async () => {
        let response = await axios.get('http://localhost:8000/venues')
        setVenues(searchBarText ? response.data.filter((venue) => venue.name.includes(searchBarText)) : response.data)
        console.log(response.data)
    }

    useEffect(() => {
        getVenues()
    }, [])

    return (
        <div className="eventListContainer">
            <SearchBar 
                searchBarText={searchBarText}
                setSearchBarText={setSearchBarText}
                onSubmit={getVenues}/>
            {venues && venues.map((venue) => (
                <VenueListItem key={venue.id} venue={venue} />
            ))}
        </div>
    )
}