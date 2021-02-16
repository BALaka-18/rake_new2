import {MDBContainer, MDBFooter} from "mdbreact";
import {Fragment} from "react";
import ExampleForm from "../ExampleForm";
import GithubCorner from "../GithubCorner";
import PreviewSection from "../PreviewSection";

const IntroPage = () => {
    return (
        <Fragment>
            <PreviewSection />
            <ExampleForm />
            <div className="footer text-center mt-3">
                <MDBContainer fluid>
                    <p className='py-2' >Want To Contribute? Have a better idea to enhance our library ? Click on the top right corner of this page.</p>
                </MDBContainer>
            </div>

            <GithubCorner />
        </Fragment>
    )
}
export default IntroPage;