
import './App.css';
import React from 'react';
class Wars extends React.Component{
  render(){
    return <li>{this.props.itemContent}</li>
  }
}

class Starwars extends React.Component{
   constructor(props){
    super(props)
      this.state = {
      name: null,
      height: null,
      gender: null,
      image: null,
      affiliations: [],
      located: false
      }
    }
     componentDidMount() {
        this.generateContent();
    }
    generateContent(){
      let num = Math.round(Math.random() * 88);
      let url = `https://raw.githubusercontent.com/akabab/starwars-api/refs/heads/master/api/id/${num}.json`;
      fetch(url)
      .then(response => response.json())
      .then(data => {
        console.log(data)
      this.setState({
      name: data.name,
      height: data.height,
      gender: data.gender, 
      image: data.image,
      affiliations: data.affiliations,
      located: true

      });
      });
     
    }
  render(){
    let starContent = this.state.affiliations.map((item, i) => {
      return <Wars key={i} itemContent={item}/>
    })
   return(
  
      <div>
       
        {
           this.state.located &&
          <div>
        
        <h1>{this.state.name} </h1>
        <p>{this.state.height}</p>
        <p>{this.state.gender}</p>
        <img src={this.state.image} alt=''></img>
        <ul>
          {starContent}
        
        </ul>
        </div>
        }
        <button type='button' onClick={() => this.generateContent()}>Generate Content</button>
      </div>
      
    );
    }
    
  }

function App() {
  return (
    <header className='App-header'>
    <div className="App">
      <Starwars/>
    
    </div>
    </header>
  );
}

export default App;
