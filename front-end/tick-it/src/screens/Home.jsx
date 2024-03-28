import { useNavigate } from "react-router-dom"
import axios from "axios"
import { useEffect, useState } from "react"
import EventListItem from "../components/EventListItem"

export default function Home() {

    const [events, setEvents] = useState([])

    let navigate = useNavigate()
    
    const getEvents = async () => {
        let response = await axios.get('http://localhost:8000/events')
        setEvents(response.data)
        console.log(response.data)
    }

    useEffect(() => {
        getEvents()
    }, [])

    // From JS Documentation
    const getRandomInt = (max) => {
        return Math.floor(Math.random() * max);
    }

    return (
        <div className="homeScreenContainer">

            <h2>Featured Event:</h2>
            {
                events.length && (
                    <EventListItem event={events[getRandomInt(events.length - 1)]}/>
                )
            }
            

            <p>
                Hey there, welcome to Tickit - where fun never stops! 
                Get ready to explore the coolest venues and hottest events just for you! 
                From epic concerts to awesome sports games, Tickit's got the tickets to your next big adventure. 
                Let's make some unforgettable memories, one tickit at a time!
            </p>
            <button 
                className="goldman-regular"
                onClick={() => navigate('/venues')}>Get started!</button>
        </div>
    )
}