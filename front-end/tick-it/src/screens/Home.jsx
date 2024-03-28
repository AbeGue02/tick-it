import { useNavigate } from "react-router-dom"

export default function Home() {
    // Might be repurposed to a login screen. For right now, it just takes the user to see venues
    let navigate = useNavigate()
    
    return (
        <div className="homeScreenContainer">
            <p>Hey there, welcome to Tickit - where fun never stops! 
                Get ready to explore the coolest venues and hottest events just for you! 
                From epic concerts to awesome sports games, Tickit's got the tickets to your next big adventure. 
                Let's make some unforgettable memories, one tickit at a time!</p>
            <button 
                className="goldman-regular"
                onClick={() => navigate('/venues')}>Get started!</button>
        </div>
    )
}