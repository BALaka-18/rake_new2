import { Fragment } from "react";
import ExampleForm from "../ExampleForm";
import GithubCorner from "../GithubCorner";
import PreviewSection from "../PreviewSection";

const IntroPage = () => {
    return (
        <Fragment>
            <PreviewSection />
            <ExampleForm />
            <GithubCorner />
        </Fragment>
    )
}
export default IntroPage;