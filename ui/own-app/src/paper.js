import React,{Component} from 'react';
import {variables} from './Variables.js';

export class paper extends Component{

    constructor(props){
        super(props);

        this.state={
            papers:[],
            Creator:1,
            modalTitle:"",
            PaperName:"",
            PaperId:0,
            saved_file:"",
            DateOfCreating:"",
            SavedPath:variables.PHOTO_URL,


            PaperIdFilter:"",
            PaperNameFilter:"",
            papersWithoutFilter:[]
        }
    }

    refreshList(){

        fetch(variables.API_URL+'/paper')
        .then(response=>response.json())
        .then(data=>{
            this.setState({papers:data});
        });
    }

    componentDidMount(){
        this.refreshList();
    }

    changePaperName =(e)=>{
        this.setState({PaperName:e.target.value});
    }
    changeDateOfCreating =(e)=>{
        this.setState({DateOfCreating:e.target.value});
    }

    addClick(){
        this.setState({
            modalTitle:"Add Paper",
            Creator:1,
            PaperId:0,
            PaperName:"",
            DateOfCreating:"",
            saved_file:""
        });
    }
    editClick(pap){
        this.setState({
            modalTitle:"Edit Paper",
            Creator:pap.Creator,
            PaperId:pap.PaperId,
            PaperName:pap.PaperName,
            DateOfCreating:pap.DateOfCreating,
            saved_file:pap.saved_file
        });
    }

    createClick(){
        fetch(variables.API_URL+'/paper',{
            method:'POST',
            headers:{
                'Accept':'application/json',
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                Creator:this.state.Creator,
                PaperName:this.state.PaperName,
                DateOfCreating:this.state.DateOfCreating,
                saved_file:this.state.saved_file
            })
        })
        .then(res=>res.json())
        .then((result)=>{
            alert(result);
            this.refreshList();
        },(error)=>{
            alert('Failed');
        })
    }


    updateClick(){
        fetch(variables.API_URL+'/paper',{
            method:'PUT',
            headers:{
                'Accept':'application/json',
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                Creator:this.state.Creator,
                PaperId:this.state.PaperId,
                PaperName:this.state.PaperName,
                DateOfCreating:this.state.DateOfCreating,
                saved_file:this.state.saved_file
            })
        })
        .then(res=>res.json())
        .then((result)=>{
            alert(result);
            this.refreshList();
        },(error)=>{
            alert('Failed');
        })
    }

    deleteClick(id){
        if(window.confirm('Are you sure?')){
        fetch(variables.API_URL+'/paper/'+id,{
            method:'DELETE',
            headers:{
                'Accept':'application/json',
                'Content-Type':'application/json'
            }
        })
        .then(res=>res.json())
        .then((result)=>{
            alert(result);
            this.refreshList();
        },(error)=>{
            alert('Failed');
        })
        }
    }

    fileUpload=(e)=>{
        e.preventDefault();

        const formData=new FormData();
        formData.append("file",e.target.files[0],e.target.files[0].name);

        fetch(variables.API_URL+'/paper/savefile',{
            method:'POST',
            body:formData
        })
        .then(res=>res.json())
        .then(data=>{
            this.setState({saved_file:data});
        })
    }

    render(){
        const {
            papers,
            modalTitle,
            Creator,
            PaperId,
            PaperName,
            DateOfCreating,
            SavedPath,
            saved_file
        }=this.state;

        return(
<div>
    <table className="table table-striped">
    <thead>
    <tr>
        <th>
            PaperId
        </th>
        <th>
            PaperName
        </th>
        <th>
            DOC
        </th>
        <th>
            Files Links
        </th>
        <th>
            Files Download
        </th>
    </tr>
    </thead>
    <tbody>
        {papers.map(pap=>
            <tr key={pap.PaperId}>
                <td>{pap.PaperId}</td>
                <td>{pap.PaperName}</td>
                <td>{pap.DateOfCreating}</td>
                <td>
                <a href={variables.API_URL+pap.saved_file}>{pap.saved_file}</a>
                </td>
                <td>
                <a href={variables.MEDIA+pap.saved_file} download> Download </a>
                </td>
            </tr>
            )}
    </tbody>
    </table>

<div className="modal fade" id="exampleModal" tabIndex="-1" aria-hidden="true">
<div className="modal-dialog modal-lg modal-dialog-centered">
<div className="modal-content">
   <div className="modal-header">
       <h5 className="modal-title">{modalTitle}</h5>
       <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"
       ></button>
   </div>

   <div className="modal-body">
    <div className="d-flex flex-row bd-highlight mb-3">

     <div className="p-2 w-50 bd-highlight">

        <div className="input-group mb-3">
            <span className="input-group-text">Pap Name</span>
            <input type="text" className="form-control"
            value={PaperName}
            onChange={this.changePaperName}/>
        </div>



        <div className="input-group mb-3">
            <span className="input-group-text">DOC</span>
            <input type="date" className="form-control"
            value={DateOfCreating}
            onChange={this.changeDateOfCreating}/>
        </div>


     </div>
     <div className="p-2 w-50 bd-highlight">
         <img width="250px" height="250px"
         src={SavedPath+saved_file}/>
         <input className="m-2" type="file" onChange={this.fileUpload}/>
     </div>
    </div>

    {PaperId==0?
        <button type="button"
        className="btn btn-primary float-start"
        onClick={()=>this.createClick()}
        >Create</button>
        :null}

        {PaperId!=0?
        <button type="button"
        className="btn btn-primary float-start"
        onClick={()=>this.updateClick()}
        >Update</button>
        :null}
   </div>

</div>
</div>
</div>


</div>
        )
    }
}
