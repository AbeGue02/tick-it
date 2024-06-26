import { useNavigate } from "react-router-dom"
import { Link } from 'react-router-dom'

export default function Header() {
    // Contains buttons to venues and event screens
    
    let navigate = useNavigate()

    return (
        <header className="headerContainer">
            
            <div className="logo">
                <h1 onClick={() => navigate('/')}>Tick-IT</h1>
                <h1 onClick={() => navigate('/')}>Tick-IT</h1>
                <h1 onClick={() => navigate('/')}>Tick-IT</h1>
            </div>
        
            <nav>
            <button onClick={() => navigate('/venues')}>Venues</button>
            <button onClick={() => navigate('/events')}>Events</button>
            </nav>
        </header>
    )
}